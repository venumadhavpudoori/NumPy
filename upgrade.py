class UpgradeManager:
    def __init__(self, current_version, target_version):
        self.current_version = current_version
        self.target_version = target_version
        self.upgrade_steps = {
            "1.0": self.upgrade_to_1_1,
            "1.1": self.upgrade_to_1_2,
            "1.2": self.upgrade_to_2_0,
        }
    
    def execute_upgrade(self):
        """Execute all necessary upgrade steps"""
        current = self.current_version
        
        while current != self.target_version:
            if current in self.upgrade_steps:
                print(f"Upgrading from {current}...")
                self.upgrade_steps[current]()
                current = self.get_next_version(current)
            else:
                raise ValueError(f"No upgrade path from {current}")
        
        print("Upgrade completed successfully!")
    
    def upgrade_to_1_1(self):
        """Upgrade database schema to 1.1"""
        print("  - Adding new columns...")
    
    def upgrade_to_1_2(self):
        """Upgrade to 1.2"""
        print("  - Migrating data...")
    
    def upgrade_to_2_0(self):
        """Upgrade to 2.0"""
        print("  - Restructuring tables...")
    
    def get_next_version(self, version):
        versions = ["1.0", "1.1", "1.2", "2.0"]
        idx = versions.index(version)
        return versions[idx + 1] if idx + 1 < len(versions) else version


# Usage
if __name__ == "__main__":
    upgrader = UpgradeManager("1.0", "2.0")
    upgrader.execute_upgrade()